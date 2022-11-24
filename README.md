# Final Project

## 1. 팀원 정보 및 업무 분담 내역

- 김지현 (조장) - Profile, Tinder, Signup / Login, Recommend Algorithm

- 최지훈 - HomeView, DetailView, Frontend Overall

- 최종현 - CommunityView, Genre Recommend, Data Filter

## 2. 실행 환경

- 프로젝트 기간 : 2022.11.16 ~ 2022.11.25

- Python 3.9.X

- Django 3.2.X

- Node.js 16.X

- Vue 2

- ```python
  cd final-pjt-back/
  cd final-pjt-front/
  ```

- ```python
  # front
  npm i
  npm run serve
  # back
  python -m venv venv
  source venv/Script/activate
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py loaddata movie.json genre.json
  python manage.py runserver
  ```

## 3. 목표 서비스 구현 및 실제 구현 정도

- 각 개인의 성향에 맞는 영화 추천 서비스 구현

- 영화 데이터 기반 영화 추천 (약 200개의 영화)

- 여러 사람들과 소통이 가능한 커뮤니티 구현

- 각 유저의 선호도를 활용한 추천 알고리즘 구현

- 다만, 댓글 작성시 댓글 좋아요와 대댓글의 시간 부족으로 구현 불가

- 틴더뷰에서 이미지 클릭시 나오는 모달에서 장르로 이동하는 버튼 기능 구현 하기에는 시간 부족으로 구현 불가

- 검색시에 검색 결과에 대한 필터링을 더 세세하게 나누지 못한 부분이 존재

- 실시간 박스오피스를 구현하는 과정에서 네이버 영화 검색 API를 불러오는 과정에서 Vue에서 axios를 불러올 때 Django를 거치지 않고 불러오자 계속해서 CORS POLYCY에 대한 문제가 발생하여 구현 불가

## 4. 데이터베이스 모델링 (ERD)

![preview url image](README_jihyun/00e97b6ed6d458fca0b853c323bc98004d344ffb.png)

## 5. 영화 추천 알고리즘에 대한 기술적 설명

* 사용자가 좋아하는 영화 데이터를 바탕으로 선호 장르 분석 (백엔드-장고)
  
  1. 틴더 및 영화 디테일 페이지에서 좋아요 버튼 클릭 
  
  2. 해당 영화의 장르에 대한 선호도 점수를 유저 정보에 저장
  
  3. 장르 선호도 Top3 Pick 
     
     : 이중 for문과 비교를 이용하여 1위, 2위, 3위 설정
     
     : 공동 순위 발생 시 기존의 값이 우선 순위
     
      (순서가 없다는 딕셔너리의 특징으로 기존 값이 우선 순위라고 고정해도 for문을 돌때 순서가 변경되어 사용자에게 다양한 영화 추천 가능 )
  
  4. Top3 장르의 선호도 점수 비율로 변환
  
  5. 추천할 영화 50개를 (4)에서 구한 비율로 장르 분배
  
  6. 이를 {장르1: 영화수, 장르2: 영화수, 장르3: 영화수} 딕셔너리 형태로 user 정보에 저장 (genre_recommend_dict)

```javascript
import random
import math
@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def recommend(request):
    username = request.user.username
    person = get_object_or_404(get_user_model(), username=username)
    person_genre_dict = person.genre_dict


    # 장르 선호 순으로 배열 [1등, 2등, 3등] = [[장르, 점수], [장르, 점수], [장르, 점수]]
    person_genre = [[0, 0], [0, 0], [0, 0]]
    for key, val in person_genre_dict.items():
        for grade in range(3):
            if person_genre[grade][1] < val:
                person_genre[grade][0] = key
                person_genre[grade][1] = val
                break
            elif person_genre[grade][1] == val:
                if (grade == 0 or grade == 1) and person_genre[grade + 1][1] != val:
                    person_genre[grade][0] = key
                    person_genre[grade][1] = val
                    break
                person_genre[grade][0] = key
                person_genre[grade][1] = val



    # 각 등수별 불러올 영화수
    total = person_genre[0][1] + person_genre[1][1] + person_genre[2][1]
    first_cnt = round((person_genre[0][1] / total) * 50)
    second_cnt = round((person_genre[1][1] / total) * 50)
    third_cnt = round((person_genre[2][1] / total) * 50)
    if first_cnt + second_cnt + third_cnt > 50:
        first_cnt -= abs(50 - (first_cnt + second_cnt + third_cnt))
    elif first_cnt + second_cnt + third_cnt < 50:
        first_cnt += abs(50 - (first_cnt + second_cnt + third_cnt))


    person.genre_recommend_dict = {}
    person.genre_recommend_dict[str(person_genre[0][0])] = first_cnt
    person.genre_recommend_dict[str(person_genre[1][0])] = second_cnt
    person.genre_recommend_dict[str(person_genre[2][0])] = third_cnt

    person.save()
    serializer = ProfileSerializer(person)
    return Response(serializer.data)
```

* Django에서 받은 데이터를 바탕으로 JS에서 getters에 회원 맞춤 영화 저장
  
  1. user에 저장된 genre_recommend_dict ({장르1: 영화수, 장르2: 영화수, 장르3: 영화수}) 순회
  
  2. 해당 장르와 일치하는 영화 우선 필터 
     
     - 임의 리스트에 하나씩 추가
  
  3. 영화의 중복을 막기 위한 조건문 추가
     
     * 한 영화에 장르가 여러개가 있는 경우가 많으므로 장르별로 영화를 뽑을 때 중복된 경우가 많음
     - 이미 추가되어 있는 영화는 더이상 추가하지 않는다.
  
  4. 해당 장르(key값)의 영화를 저장된 영화 수(value)만큼 랜덤으로 뽑기
     
     - lodash의 _.sampleSize(배열, 갯수) 이용
  
  5. 장르별로 pick한 영화 리스트 3개를 하나의 리스트로 합하기
     
     - Spread Syntax 이용
     
     - 최종리스트.push(...3개의 장르 리스트 각각)

```javascript
// store/index.js

// 회원 맞춤 영화
    getRecommendMovie(state) {
      const getRecommendMovie = [] // 장르별 영화 
      for (const genre_id in state.user.genre_recommend_dict) {
        // recMovie: 장르별 영화 리스트
        const recMovie = state.movies.filter((movie) => {
          if (movie.genres.includes(Number(genre_id))) { // 만약 해당 장르일 때
            return !getRecommendMovie.includes(movie) // 지금까지 최종 리스트(getRecommendMovie)에 없으면 포함 (중복제
          }
        })
        getRecommendMovie.push(..._.sampleSize(recMovie, state.user.genre_recommend_dict[genre_id]))
      }
      return getRecommendMovie
    },
```

- 간단한 영화 추천 알고리즘으로는 매년 동일한 월에는 비슷한 맥락의 영화가 개봉하므로 그에 따라서 현재 월과 같은 월에 개봉한 영화를 추천함

- 가벼운 마음으로 영화를 시청하는 것을 선호하는 유저들을 위해서 런타임(상영시간)이 짧은 영화 (<= 90)인 영화를 추천함

## 6. 서비스 대표 기능에 대한 설명

### 1) 틴더 (Tinder)

* 틴더는 소셜 디스커버리 어플리케이션으로 "스와이핑" 어플리케이션이다.

* 기본적인 기능으로 오른쪽으로 스와이프하면 호감, 왼쪽으로 스와이프하면 다른 사람 사진, 위로 스와이프하면 super(아주 좋아요)로 넘어갈 수 있다.

* 이러한 "스와이핑" 기능을 이용하여 우리는 사용자의 영화에 대한 선호도를 조사하였다.

* 오른쪽으로 스와이프하면 좋아요, 왼쪽으로 스와이프하면 다른 영화로 넘어간다.

* 내부 기능에서 위로 스와이핑을 제거 할수 없어서 super도 좋아요 function으로 링크를 걸어 두어 오류를 없앴다.

* 또한 영화의 자세한 설명을 알고싶을땐 제목을 클릭하여 영화의 줄거리를 알 수 있게 모달을 설정했다.

* 이렇게 좋아요한 데이터를 바탕으로 장르 선호도를 조사하였다.

* 사용자 데이터 분석을 위해 단순히 좋아요 버튼만을 만든것이 아니라 "스와이핑" 기능으로 사용자의 편의와 흥미를 고려하였다.

### 2) 깔라 (Toggle)

- 레트로한 느낌을 주기위한 흑백스타일과 일반 컬러스타일를 스위칭할수있는 토클키다.

- 디포트는 흑백이고 컬러 페이지를 원하는 유저를 위해 우측 상단에 '깔라' 버튼을 클릭하면 컬러스타일로 변경된다.

- 레트로라는 컨셉이 취향이 있을 수 있으니 컬러스타일도 추가하여 사용자가 느낄 수 있을 불편함을 줄였다.

- ```
  :class="{'oldColor': old_color}
  
  style =>
  .oldColor {
    filter: grayscale(1);
  }
  ```

- 처음은 간단하게 전역에  클래스로 oldColor를 만들고 버튼과 연동하여 모든 자식 컴포넌트에 흑백인 grayscale을 적용시켰다

- 하지만 여기서 TopBar(모달)과 틴더가 오류를 일으켰다.

- 흑백스타일을 키면 TopBar는 페이지 마다 밑 부분이 잘리기 시작했고 틴더는 아예 화면에 나오지 않았다.

- 여러 고민을하고 콘솔을 본 결과 부트스트랩과 vue-tinder를 설치하여 사용했던 내부  클래스에서 충돌이 났을 것이다 라고 판단을 하고 클래스 적용 위치와 예외를 두어서 오류를 막아보기로 했다.

- 먼저 TobBar는 가장 부모 컴포넌트인 App.vue 바로 밑에 있으므로 TopBar 컴포넌트와 다른 자식 컴포넌트인 router-view에 먼저 적용시키고 TopBar는 props로 넘겨주었다.

- ```
  .oldColor :not(.tinder-body){
    filter: grayscale(1);
  }
  ```

- 틴더부분에서는 완전히 제외해야 하므로, 스타일에 :not(.tinder-body)를 사용하여 틴더에서는 적용이 되지 않게 하였다.

## 7. 기타 (느낀 점, 후기 등)

[지현]

- 처음에는 처음부터 정확한 계획을 세워 진행하려 했지만 진행해봐야 알 수 있는 것들이 많았다. 그래서 매일매일 아침, 오후 **회의를 통해 진행 단계를 파악하고 계획을 수정하는 것이 중요**하다고 느꼈다. **Notion을 활용하여 계획과 자료를 공유하고 기록**하는 것 역시 중요하였다. 완벽하게 활용하지는 못했지만 이 덕분에 현재 진행 상황을 한눈에 파악하고 팀간의 소통이 수월했던 것 같다.

- 이번 프로젝트를 통해 한학기 동안 배운것(Django, Vue, ...)들 각각이 어떻게 사용되고 서로 어떻게 연결되는지 파악할 수 있었다.

- 그리고 구글링을 잘 해서 더욱 유익한 코딩 정보를 얻는 것이 중요하다는 것을 알았다. (전에는 구글링 하지 않고 배운것을 응용하려고 함)

- 처음에 model과 serializer부분을 작성하는 것이 어려웠다. Django때 이 부분이 정확히 이해가 되지 않아 어려움을 많이 겪었은데 그래도 프로젝트를 진행하며 여전히 완벽히 이해한 것은 아니지만 그래도 전보다 많이 이해하는 것 같다.

- profile부분을 작성하며 역참조를 많이 해야했는데 나는 **account에 작성한 게시글, 댓글, 좋아요한 영화 모두를 ProfileSerializer로 만들어서 저장**하여 data를 주고 받았더니 다른 사람들에 비해 수월하게 진행하였다.

- 하지만 마지막에 싫어요한 영화 필드를 추가하려고 했는데 user정보가 자꾸 받아지지 않고 해당 필드를 User에 사용할 수 없다는 오류가 발생하여 시간이 없어서 포기하였다.

- 좋아요한 영화, 싫어요한 영화 필드 두개 모두를 만든 조의 모델을 봤는데 영화에 해당 필드를 만들었다.

- 영화 추천 알고리즘을 만드는 과정에서 오류가 발생하였다. key오류였는데, 최종적으로는 중복되는 영화는 임의 리스트에 넣지 않도록 했지만 처음에는 그 과정이 없어서 중복되는 영화가 들어갔다. 그래서 영화들을 for문으로 component에 props로 보내는데 이때 중복되는 영화로 인해 key값이 중복이 되어 오류가 발생했다.

[지훈]

- 최종 프로젝트 이전에 2번의 관통 프로젝트에서 협동 프로젝트를 경험해보았지만 최종 프로젝트는 그전과는 차원이 달랐다. 이전의 프로젝트는 주어진 것만 구현하는 것을 목표로 서로의 임무 분담도 금방했었고, 각자 분담이 되면 바로 작업을 시작할 수 있었다. 하지만 최종 프로젝트는 주어진 목표는 적고 우리가 계획하고 수정하며 만들어 가는 것이란게 매우 생소했다.

- 먼저 매일 아침 회의를 하면서 진행단계와 임무 분담을 정하고 중간중간에도 서로 소통하면서 무엇이 더 좋은지, 어떻게 하면 문제를 해결할 수 있는지 등등 지속적인 커뮤니케이션이 협동 프로젝트에서 얼마나 중요한지 다시 느낄 수 있었다.

- 또한 이번 프로젝트는 내가 그동안 배운 모든 지식을 총 동원하고 부족한것은 인터넷 검색과 책도 보면서 하나의 기능을 구현하는데까지 많은 것을 느낄 수 있었다. 밤이 될 때까지 기능 하나를 구현 못하면서  내가 정말 못난이 같다고 느끼면서도 허탈감이 클때도 있지만, 새벽까지 고생하면서 문제를 해결하고 기능이 정상작동하는것을 보며 큰 성취감과 이 길을 온 것에 대하여 후회하지 않고 자신감을 얻었다.

[종현]

- 기존의 간단한 관통프로젝트에서는 해당 주나 해당 학습 기간에 학습한 내용으로 프로젝트를 진행하는 것이다 보니 배운 내용에 대해서 기억도 잘 나고 어려운 부분이 적었지만, 페어와 함께 진행하는 큰 프로젝트의 경우에는 전체 배운 내용을 사용함과 동시에 추가적으로 학습을 진행하면서 프로젝트를 완성해야했기에 더욱 더 많이 어려움이 있었다. 

- 기본적으로 notion을 활용하면서 모든 작업 상황을 정리하고 관리하면서 체계적으로 프로젝트를 진행하려고 했으나, 처음 진행하는 프로젝트이기도 했고 완전하게 익숙하지 않은 notion을 사용하기에는 부족한 부분이 있었다. 다만, 매일 아침마다 진행상황과 진행해야하는 부분에 대해서 회의를 진행하여 프로젝트를 진행할 수 있었다. 지속적으로 소통을 많이 하고, 의논도 많이 하면서 프로젝트는 진행하는 과정에서 비효율적으로 시간을 보내지 않았기때문에 다수의 팀프로젝트에서는 확실히 끊임없이 소통을 통해 방향성을 제대로 잡아가야 한다는 것을 다시금 배울 수 있게 되었다.

- 기본적으로 데이터를 불러오기 위해서 JSON데이터를 받아오기 위해서 init.py를 작성하는 방법을 구글링을 통해 검색하여 교수님의 설명 이전에 이미 영화 json파일을 가지고 프로젝트를 진행을 하기 위해서 준비를 했다.

- 기초적인 전체 영화데이터를 불러오고 장르데이터를 불러오는 과정을 진행하고 난 뒤에 팀원끼리 기능별로 작업을 구분하면서 간단하게 전체 영화 목록을 불러오는 업무를 맡게 되었다. 

- 그 후에는 커뮤니티 기능을 사용하기 위해서 게시글 작성 및 댓글 기능을 구현을 진행했다. 다만, 댓글을 수정하는 기능을 구현하기 위해서는 하나의 컴포넌트에서 작성과 리스트 수정을 모두 구현하니 오류가 발생하여, 다시 컴포넌트를 분리시켜 등록을 시키는 과정에서 시간이 생각보다 소모되었다. 그 후에는 댓글 수정은 페이지 이동이 아닌 JS을 통해 수행해야하므로 이 기능을 구현하기 위한 과정에서도 어려움이 존재했다. 댓글 폼을 수정버튼을 누르면 댓글이 표시되는 부분에 나오게 하고 완료시 다시 댓글을 나오게 하는 기능을 구현하기 위해서 많이 검색을 진행했다. 그 부분은 수정한다는 변수를 생성해 수정을 버튼을 눌렀을 때와 누르지않았을 때마다 그 변수의 true false값을 변경시켜 v-if를 활용하여 구현할 수 있었다.

- 영화 디테일 페이지에서도 별점 기능을 구현하기 위해서 npm i vue-rating-stars를 설치하여 별점을 구현하고 이를 db에 저장하기 위해서 movies에 새로운 Rank라는 모델을 생성하고 이 정보를 유저에게 저장해주기 위해서 accounts serializer에 추가하면서 역참조까지 가능하게 구현하였다.

- 그 외에도 hover라던지 다양한 css기능을 추가하면서 웹에 대한 지식을 키울 수 있었다.

- 다른 2명의 팀원이 많은 양을 미리 끝내주어 기능 구현에 있어서 큰 어려움은 없이 할 수 있었지만, 아직 온전히 기능을 구현하는데 사용하고 학습한 내용이 습득되었는지에 대해서는 아쉬운 부분이 있어 지속적인 학습이 필요할 것이라고 생각된다. 

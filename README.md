# Final Project

## 1. 팀원 정보 및 업무 분담 내역

* 김지현 (조장) - Profile, Tinder, Signup / Login, Recommend Algorithm

* 최지훈 - HomeView, DetailView, Frontend Overall

* 최종현 - CommunityView, Genre Recommend, Data Filter



## 2. 목표 서비스 구현 및 실제 구현 정도



## 3. 데이터베이스 모델링 (ERD)

![preview url image](README_jihyun/00e97b6ed6d458fca0b853c323bc98004d344ffb.png)





## 4. 영화 추천 알고리즘에 대한 기술적 설명

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
      const getRecommendMovie = []
      for (const genre_id in state.user.genre_recommend_dict) {
        // console.log(genre_id)
        const recMovie = state.movies.filter((movie) => {
          // console.log(movie.genres)
          if (movie.genres.includes(Number(genre_id))) {
            return !getRecommendMovie.includes(movie)
          }
        })
        // console.log(recMovie)
        getRecommendMovie.push(..._.sampleSize(recMovie, state.user.genre_recommend_dict[genre_id]))
      }
      return getRecommendMovie
    },
```





## 5. 서비스 대표 기능에 대한 설명

### 1) 틴더 (Tinder)

* 틴더는 소셜 디스커버리 어플리케이션으로 "스와이핑" 어플리케이션이다.

* 오른쪽으로 스와이프하면 호감, 왼쪽으로 스와이프하면 다른 사람 사진으로 넘어갈 수 있다.

* 이러한 "스와이핑" 기능을 이용하여 우리는 사용자의 영화에 대한 선호도를 조사하였다.

* 오른쪽으로 스와이프하면 좋아요, 왼쪽으로 스와이프하면 다른 영화로 넘어간다.

* 이렇게 좋아요한 데이터를 바탕으로 장르 선호도를 조사하였다.

* 사용자 데이터 분석을 위해 단순히 좋아요 버튼만을 만든것이 아니라 "스와이핑" 기능으로 사용자의 편의와 흥미를 고려하였다.

* vue tinder Guide : https://shanlh.github.io/vue-tinder/guide/getting-started.html#installation
  
  * vue-tinder 설치하여 사용
  
  * npm install vue-tinder --save

 

### 2) 깔라 (Toggle)

* 현재 아이폰, 인스타그램 등 다양한 곳에서 사용하는 다크모드를 응용

* 토글을 이용하여 스타일을 변경시켜 칼라와 흑백으로 디스플레이가 변경되는 기능 추가

* 사용자 선호도에 따라 디스플레이 스타일 변경 가능

* 시각적 흥미 유발



## 6. 기타 (느낀 점, 후기 등)

#### [지현]

* 처음에는 처음부터 정확한 계획을 세워 진행하려 했지만 진행해봐야 알 수 있는 것들이 많았다. 그래서 매일매일 아침, 오후 **회의를 통해 진행 단계를 파악하고 계획을 수정하는 것이 중요**하다고 느꼈다. **Notion을 활용하여 계획과 자료를 공유하고 기록**하는 것 역시 중요하였다. 완벽하게 활용하지는 못했지만 이 덕분에 현재 진행 상황을 한눈에 파악하고 팀간의 소통이 수월했던 것 같다. 

* 이번 프로젝트를 통해 한학기 동안 배운것(Django, Vue, ...)들 각각이 어떻게 사용되고 서로 어떻게 연결되는지 파악할 수 있었다.

* 그리고 구글링을 잘 해서 더욱 유익한 코딩 정보를 얻는 것이 중요하다는 것을 알았다. (전에는 구글링 하지 않고 배운것을 응용하려고 함)

* 처음에 model과 serializer부분을 작성하는 것이 어려웠다. Django때 이 부분이 정확히 이해가 되지 않아 어려움을 많이 겪었은데 그래도 프로젝트를 진행하며 여전히 완벽히 이해한 것은 아니지만 그래도 전보다 많이 이해하는 것 같다.

* profile부분을 작성하며 역참조를 많이 해야했는데 나는 **account에 작성한 게시글, 댓글, 좋아요한 영화 모두를 ProfileSerializer로 만들어서 저장**하여 data를 주고 받았더니 다른 사람들에 비해 수월하게 진행하였다. 

* 하지만 마지막에 싫어요한 영화 필드를 추가하려고 했는데 user정보가 자꾸 받아지지 않고 해당 필드를 User에 사용할 수 없다는 오류가 발생하여 시간이 없어서 포기하였다.

* 좋아요한 영화, 싫어요한 영화 필드 두개 모두를 만든 조의 모델을 봤는데 영화에 해당 필드를 만들었다.  

* 영화 추천 알고리즘을 만드는 과정에서 오류가 발생하였다. key오류였는데,  최종적으로는 중복되는 영화는 임의 리스트에 넣지 않도록 했지만 처음에는 그 과정이 없어서 중복되는 영화가 들어갔다. 그래서 영화들을 for문으로 component에 props로 보내는데 이때 중복되는 영화로 인해 key값이 중복이 되어 오류가 발생했다.

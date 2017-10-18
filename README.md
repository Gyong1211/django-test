# Django Test

```
# Django project

django-test/
	.git
	.gitignore
	.python-version
	
	wed_test/		<django project>
		config/
		post/		<django app>
		template/
			post/

	media/			<django media storage>
		post/
			<post image>		
```


```
- Post model
	title
	photo (media/post/ 경로로 사진 
	content
	created_date
```


1. Github repository 생성 (`django-test`)
2. 환경 세팅(`pyenv`, `git`, `pycharm`)
3. django setting file 설정 (template dir, media root) - commit: `First commit`
3. `post` app 만들기
4. `Post` Model 생성 및 admin에서 3개의 object를 만들기(object의 title이 보이도록 설정)
5. `post_list` view, template 생성 및 url(`post/`) 연결 - commit: post\_list 기능 추가
6. `post_detail` view, template 생성 및 url(`post/1/`) 연결 - commit: post detail 기능 추가
7. `post_create` view, template 생성 및 url(`post_create/`) 연결 - commit: post create 기능 추가
8. `post_delete` view 생성(**POST**요청이 오는 경우 post object 삭제, **GET**인 경우 `post_list`로 redirect), url(`post_delete/1/`) 연결, `post_list` template와 `post_detail` template에 해당하는 Post object를 삭제 할 수 있는 버튼 추가 - commit: post delete 추가

>> 가상환경은 있던걸 사용해도 상관 없음.  
>> CSS 신경 안써도 됨
>> django template tag(extends, include), Form 사용은 자유.  
>> 기존에 진행하던 Project는 참고 금지.  
>> 오류사항이 발생하면 옆사람에게 물어보거나, django document, google에 검색해서 해결  


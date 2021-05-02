from django.contrib import admin
from home.models import Question, Choice
# Register your models here.
# 테이블을 새로 만들 때는 models.py와 admin.py 둘 다 수정해야함

# 필드 순서 바꾸기
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text'] # 필드 순서 변경
#

# 각 필드 분리해서 보여주기
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Question Statement', {'fields': ['question_text']}),
#         ('Date Information', {'fields': ['pub_date']}),
#         # 필드 접어서 보여주기
#         # ('Date Information', {'fields': ['pub_date'], 'classes':['collapse]}),
#     ]

# Question과 Choice 같이 보기
# 테이블 형식으로 보여주기


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]  # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date')  # 레코드 리스트 컬럼 지정
    list_filter = ['pub_date']   # 필터 사이드 바 추가
    search_fields = ['question_text']  # 검색 박스 추가


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

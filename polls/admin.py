from django.contrib import admin

# Register your models here.

from .models import Poll

# admin.site.register(Poll)			# 1 варіант - по-замовчуванню

#class PollAdmin(admin.ModelAdmin):		# 2 варіант - зміна полів
#    fields = ['pub_date', 'question']

#admin.site.register(Poll, PollAdmin)

#class PollAdmin(admin.ModelAdmin):		# 3 варіант - багато полів та поділ на групи
#    fieldsets = [
#        (None,               {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]

#admin.site.register(Poll, PollAdmin)

#class PollAdmin(admin.ModelAdmin):		# 4 варіант - багато полів та поділ на групи + HTML(приховане поле)
#    fieldsets = [
#        (None,               {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]

#admin.site.register(Poll, PollAdmin)


from polls.models import Choice

#admin.site.register(Choice)			# 4 варіант + реєстрація Choice

#class ChoiceInline(admin.StackedInline):	# 5 варіант Poll + Choice
class ChoiceInline(admin.TabularInline):	# 5 варіант Poll + Choice + вдосконалення для Choice
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
#    list_display = ('question', 'pub_date')
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)


















from django.db import models
from django.utils.text import slugify

class Project(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True, blank=True)
	budget = models.IntegerField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Project, self).save(*args, **kwargs)

	@property
	def buget_left(self):
		expense_list = Expense_objects.filter(project=self)
		total_expense_amount = 0
		for expense in expense_list:
			total_expense_amount += expense.amount

		#temporary solution, because the form currently only allows integer amounts
		total_expense_amount = int(total_expense_amount)

		return self.budget - total_expense_amount

	@property
	def total_transactions(self):
		expense_list = Expense.objects.filter(project=self)
		return len(expense_list)

	def get_absolute_url(self):
		return '/' + self.slug


class Category(models.Model):
	project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=50)

class Expense(models.Model):
	project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=100)
	amount = models.DecimalField(max_digits=8, decimal_places=2)
	category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

	class Meta:
		ordering = ('-amount',)
	
	
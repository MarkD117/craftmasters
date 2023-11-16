from .models import Category


def categories(request):
    # Returning dictionary of all categories
    return {'categories': Category.objects.all()}
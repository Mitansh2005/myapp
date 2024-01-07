from import_export import resources
from .models import daily_log

class daily_logResource(resources.ModelResource):
  class meta:
    model=daily_log
    skip_unchanged = True
    use_bulk = True
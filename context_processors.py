import local_settings

def ga_processor(request):
  # Add google analytics

  return {'ga_account': local_settings.ga_account,}
	

def get_commit_shas(data):
    # The most recent commit SHA (after)
    latest_sha = data['after']  # '892ee96398ec9924789da8551b85ca07e65217c3'
    
    # The previous commit SHA (before)
    previous_sha = data['before']  # '896b3c2e4450f6d0ac9ba86efb0395a1819e3190'
    
    # Individual commit SHAs in the commits list
    commit_shas = [commit['id'] for commit in data['commits']]
    # ['f21e7f83c5d6ca40d1c6f19d87cd37e8f4ee74f7', 
    #  '892ee96398ec9924789da8551b85ca07e65217c3']
    
    return {
        'latest_sha': latest_sha,
        'previous_sha': previous_sha,
        'commit_shas': commit_shas
    }

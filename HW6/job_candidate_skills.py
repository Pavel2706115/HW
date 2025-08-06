required_skills = {'Python', 'Django', 'SQL', 'Git'}
candidate_skills = {'Python', 'Flask', 'Git', 'JavaScript'}

matched_skills = required_skills.intersection(candidate_skills)
missing_skills = required_skills.difference(candidate_skills)
extra_skills = candidate_skills.difference(required_skills)

print(f"Matched skills: {', '.join(matched_skills)}")
print(f"Missing skills: {', '.join(missing_skills)}")
print(f"Extra skills: {', '.join(extra_skills)}")
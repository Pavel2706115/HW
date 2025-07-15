#Input
total_academic_hours = 64
# Constants
astronomical_hour_minutes = 60
academical_hour_minutes = 40
academical_hours_per_session = 4
break_minutes_per_session = 20
#Number of sessions
num_sessions = total_academic_hours // academical_hours_per_session
#Total time in minutes
total_minutes = (total_academic_hours * academical_hour_minutes) + (num_sessions * break_minutes_per_session)
# Conversion to astronomical hours
total_astronomical_hours = total_minutes / astronomical_hour_minutes
print("Total duration in astronomical hours:", total_astronomical_hours)
    
    
import nutrionix
import sheets

exercise = nutrionix.get_user_exercise()
user_parameters = nutrionix.get_user_parameters(exercise)
exercise_stats = nutrionix.get_exercise_stats(user_parameters)
to_sheets = sheets.create_body(exercise_stats)
sheets.send_to_sheets(to_sheets)
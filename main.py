# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scoring_player1 = 'Gullit'
scoring_player2 = 'Van Basten'

goal_0 = 32
goal_1 = 54

scorers = scoring_player1 + ' ' + str(goal_0) +', ' + scoring_player2 + ' ' + str(goal_1)

report = f'{scoring_player1} scored in the {goal_0}nd minute\n{scoring_player2} scored in the {goal_1}th minute'

report_alternative = f'{scorers[0:6]} scored in the {scorers[7:9]}nd minute\n{scorers[11:21]} scored in the {scorers[22:24]}th minute'

player = 'Oleksiy Mykhaylychenko'
first_name = player[0:player.find(" ")]
last_name_len = len(player[player.find(" "):])
name_short = player[0:1] + '.' + player[player.find(" "):]
chant = (first_name + '! ') * (len(first_name) - 1) + (first_name + '!')
good_chant = chant[-1] != ' '

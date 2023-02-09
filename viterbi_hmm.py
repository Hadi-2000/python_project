# Transition Probabilities
p_ss = 2/3
p_sr = 1/3
p_rs = 1/6
p_rr = 5/6

# Initial Probabilities
p_s = 0.3
p_r = 0.7

# Emission Probabilities
p_sh = 1/3
p_sg = 2/3
p_rh = 4/7
p_rg = 3/7

moods = ['H', 'G', 'H', 'G', 'H', 'G', 'H','G','H','G']
probabilities = []
weather = []

if moods[0] == 'H':
    probabilities.append((p_s*p_sh, p_r*p_rh))
else:
    probabilities.append((p_s*p_sg, p_r*p_rg))

for i in range(1, len(moods)):
    yesterday_sunny, yesterday_rainy = probabilities[-1]
    if moods[i] == 'H':
        today_sunny = max(yesterday_sunny*p_ss*p_sh, yesterday_rainy*p_rs*p_sh)
        today_rainy = max(yesterday_sunny*p_sr*p_rh, yesterday_rainy*p_rr*p_rh)
        probabilities.append((today_sunny, today_rainy))
    else:
        today_sunny = max(yesterday_sunny*p_ss*p_sg, yesterday_rainy*p_rs*p_sg)
        today_rainy = max(yesterday_sunny*p_sr*p_rg, yesterday_rainy*p_rr*p_rg)
        probabilities.append((today_sunny, today_rainy))

for p in probabilities:
    if p[0] > p[1]:
        weather.append('S')
    else:
        weather.append('R')

print(weather)

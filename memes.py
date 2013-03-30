import re

def run(nick, message, command_prefix):
    prefixed_commands = [
        ('tidigt', '<calle> {sender} går alltid och lägger sig tidigt'),
        ('tidigt {arg}', '<calle> {arg} går alltid och lägger sig tidigt'),
        ('tidigt/me {arg}', '* {arg} går alltid och lägger sig tidigt'),
        ('nej', '<jocke-l> jag har alltid och nej, det har jag inte.\n<jocke-l> ALLITD'),
        ('allitd {arg}', '<jocke-l> jag har alltid och {arg}\n<jocke-l> ALLITD'),
        ('rullar {arg}', '{arg} rullar in som det ska\ndet går bra nu'),
        ('wannab', 'luktar wanna b amerikan'),
        ('murk( hyad)?', '☻'),
        ('lose', 'The Game.'),
        ('lök', '<Goebbels> Nu ska jag handla LÖK.'),
        ('lök {arg}', '<Goebbels> Nu ska {arg} handla LÖK.'),
        ('mr_basic', '<kobran> abobaloba baloba\n<kobran> he\'sa mr_basic\n<kobran> mr fantastic'),
        ('yo', '* Pranz joined the channel\n<Pranz> Yo\n<calle> micraft server\n<Pranz> Vad ligger den på?\n[lång tystnad]'),
        ('hybrid', '<psi-omega> i want it in mah hybrid car bitch!'),
        ('regex(es)?', 'http://i.solidfiles.net/c66.jpg'),
        ('title', 'nej'),
        ('ping', 'pong')
    ]

    commands = [('ALLITD', 'ALLITD')] + \
               [(command_prefix + cmd, answer)
                for cmd, answer in prefixed_commands]

    for command, answer in commands:
        match = re.match(command.format(arg=r'(?P<arg>.+?)') + '$', message)
        if match:
            if 'arg' in match.groupdict():
                arg = match.group('arg')
            else:
                arg = ''
            return answer.format(arg=arg, sender=nick).split('\n')



# (^|.*?\W)LÖ+K(\W.*?|$) -> #py: 'L' + 'Ö'*random.randint(2,8) + 'K'
# {myname}! -> wuh?

# ('choose {arg}', '#py: random.choice(arg.split('|')).strip()'),
# ('tyda {arg}', '{sender}: http://tyda.se/search/{qarg}'),
# ('hitta {arg}', '{sender}: www.hitta.se/LargeMap.aspx?var={qarg}'),
# ('vecka', '#py: '{0}: Vecka {1}'.format(sender, datetime.date.today().isocalendar()[1])'),
# ('jdn', '#py: '{0}: Nuvarande julian day: {1:.5f}'.format(sender, calendar.timegm(datetime.datetime.utcnow().utctimetuple())/86400.0 + 2440587.5)'),




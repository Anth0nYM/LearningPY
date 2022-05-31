import re
txt = 'medonho sua atitude medosca'
result1 = re.search(' medo ',txt,)
result2 = re.search(' #medo ',txt,)
result3 = re.search(' medo! ',txt,)
if result1 or result2 or result3 != None:
    print('Medo encontrado no seu tweet')
else:
    print('Não há medo no seu tweet')
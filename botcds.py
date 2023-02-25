import random
import pandas as pd
import json
from variables import *


#Feedback resources
# path = 'D:\dcbot'
#
# pf = pd.read_csv(path + '//pf.csv')
# ef = pd.read_csv(path + '//ef.csv', keep_default_na=False)

with open(path + '//target.json', 'r') as jsfile:
    target = json.load(jsfile)
jsfile.close()

vbabuse = ['作为一个bot， 我想用塑料小鸭打爆你的狗头', '说慢点，我狗话不是很好' , '天晴了，雨停了，你就觉得你行了。', '你这种智商看20集智慧树都补不回来',
           '等我有钱了，我就带你去最好的神经病院。', '我真的很想帮你治疗，但我是一名家庭医生，而你是一个孤儿。', '等你死了，我直接坐飞机到你的坟头，疯狂地偷吃你的贡品',
           '小学毕业了吗？ 一篇报纸读的下来吗？', '本大爹将你这弱智小儿一手击在墙上抠都抠不下来', '祝你把把对K碰对A', '如果让人犯恶心是刑事犯罪，你得死刑立即执行。',
           '脑子是个好东西，希望人人都可以有', '我把你挂到迎客松上喜迎八方贵客', '我这聊着聊着还有点饿了呢 emmm想拿你骨灰熬点稀饭', '您看我像配钥匙的是吧？行，您配几把？']

#############################
#Command Section
#############################

#A function to transform a piece of message into a dataframe
def history_df(author = '', create_at = '', content = ''):
    return pd.DataFrame({'author': [author], 'create_at': [create_at], 'content': [content]})


#A function to output the chat history of the channel that the command is sent
async def history_generator(message):
        df = pd.DataFrame({'author': [], 'create_at': [], 'content': []})
        async for msg in message.channel.history(limit = 50):
            if msg.author.bot:
                continue

            if len(msg.content) > 0:
                if msg.content[0] != '[':
                    df = pd.concat([df, history_df(msg.author, msg.created_at, msg.content)])


        df.to_csv(path + '\dchistory.csv', encoding='utf_8_sig')
        print('File generated successfully!')


#A function to add or alter reply
async def pfcreator(message):
        global pf

        temp = message.content[1:].split()
        if len(temp) < 3:
            await message.channel.send('command pfcreate usage: [pfcreate <content should include> <content reply>')

        if temp[1] not in pf[['include']].values:

            try:
                msg = pd.DataFrame({'include': [temp[1]], 'print': [temp[2]]})

                pf = pd.concat([pf, msg]).reset_index()
                pf = pf[['include', 'print']]

                pf.to_csv(path + '\pf.csv', encoding='utf_8_sig')
                await message.channel.send('New record created')
            except:
                await message.channel.send('Something is wrong')
        else:
            pf['print'][pf['include'] == temp[1]] = temp[2]
            pf = pf[['include', 'print']]
            pf.to_csv(path + '\pf.csv', encoding='utf_8_sig')
            await message.channel.send('Record altered')


#A function to set a user as the target of verbal abuse
async def fk(message):

    # Add the user name to a dictionary, describing the user being targeted and the number of times to be attacked
    target = {message.content[4:]: 5}
    with open(path + '//target.json', 'w') as jsfile:
        json.dump(target, jsfile)
    jsfile.close()

    await message.channel.send(list(target.keys())[0] + ' 我喊你一声你敢答应吗')


#A function to verbal abuse a user
async def attack(message):
    global target, vbabuse

    user = list(target.keys())[0]

    if target[user] == 0:
        target = {'temp' : 0}
        return
    else:
        target[user] -= 1
        await message.channel.send(list(target.keys())[0] + random.choice(vbabuse))


#A function to generate random number in a range
async def rdpick(message):
    response = '幸运数字就是： '

    temp = message.content[1:].split()
    print(temp, response + str(random.choice(range(int(temp[1])))))
    try:
        if len(temp) == 2:
            await message.channel.send(response + str(random.choice(range(int(temp[1])))))
        if len(temp) == 3:
            await message.channel.send(response + str(random.choice(range(int(temp[1]), int(temp[2])))))
    except:
        await message.channel.send('usage: +r <start num default 0> <end num>')





#A function to list all the commands
async def cdlst(message):
    global commandlst

    menu = ''

    for i in range(len(commandlst)):
        menu = menu + '{:<30}{:<20}{:<20}\n'.format(commandlst[i][0], commandlst[i][1], commandlst[i][2])

    await message.channel.send(menu)



#Help resources
commandlst = [['fk', '语言攻击一个用户', 'usage: [fk <@some user>', fk],
              ['r' ,  '生成一个随机数', 'usage: [r <start num default 0> <end num>', rdpick],
              ['pfcreate', '添加一条关键词检测回复', 'usage: [pfcreate <content should include> <content reply>', pfcreator],
              ['list' ,    '显示所有可用指令', 'usage: [list', cdlst]]

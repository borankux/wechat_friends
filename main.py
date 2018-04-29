import itchat
import json
import requests as rq

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])



itchat.auto_login(hotReload=True)


friends = itchat.get_friends(update=True)
friends_json = json.dumps(friends)


print "Start downloading friends ..."
fri_file = open('friends_list.js','w')
head_text = "var friendsList = \n"
tail_text = "\n export default friendsList"
fri_file.write(head_text+friends_json+tail_text)
fri_file.close()
print "Done!"

print "Start download friend head ..."
for f in friends:
	itchat.get_head_img(userName=f.UserName,picDir="head_imgs/"+f.UserName+".jpeg")
	print f.NickName+":Done"
print "Done"
itchat.run()
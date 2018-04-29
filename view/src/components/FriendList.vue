<template>
  <div class="friend-list-holder">
    <input type="text" @keydown.down="showDown" @keydown.up="showUp" v-model="currentNumber">
    <ul class="friend-list">
      <li v-for="(friend,index) in friendList" class="friend" @click="selectCurrentUser(friend)">
        <div style="float: left;" class="index">
          {{ index +1 }}
        </div>
        <div style="float: left;">
          <img :src=translateHeadIcon(friend) alt="" class="head-icon">
        </div>
        <div style="float: left;">
          <div class="title">
            {{friend.NickName}}
          </div>
          <div class="province">
            {{friend.Province}}.{{friend.City}}
          </div>
        </div>
        <div v-bind:class="{gender:true,girl:(friend.Sex===0),boy:(friend.Sex===1),alien:(friend.Sex!==1&&friend.Sex!==0)}"></div>
      </li>
    </ul>

    <div class="preview">
      <img :src="translateHeadIcon(currentUser)" alt="" >
      <h3>{{currentUser.NickName}}（{{currentUser.RemarkName}}）</h3>
      <p v-html="currentUser.Signature">
      </p>
    </div>
  </div>
</template>

<script>
    import FriendData from '@/data/friends_list'
    export default {
        name:'friend-list',
        data () {
          return {
            currentUser:FriendData[0],
            currentNumber:0
          }
        },
       mounted () {
          console.log(FriendData[271]);
       },
       computed:{
          friendList:function(){
            return FriendData
          },
       },
       watch:{
          currentNumber:function(cv,ov){
            this.currentUser = FriendData[cv]
          }
       },
      methods:{
          translateHeadIcon:function(friend){
            return "http://localhost:8082/"+friend.UserName+".jpeg";
          },
        selectCurrentUser:function(friend){
            this.currentUser = friend;
        },
        showUp:function(){
            if(this.currentNumber>0){
              this.currentNumber --;
            }
        },
        showDown:function(){
            if(this.currentNumber<FriendData.length){
              this.currentNumber++;
            }
        }
      }
    }å
</script>

<style scoped>
  .friend-list{
    display: block;
    list-style: none;
    padding: 0px;
    width: 500px;
  }

  .friend-list>li{
    display: block;
    padding: 0px;
    height: 50px;
    margin: 10px auto;
    box-shadow: 0px 0px 6px 2px #ccc;
    border-radius: 3px;
  }

  .index{
    height: 50px;
    width: 50px;
    line-height: 50px;
    text-align: center;
    background-color: rgba(250, 194, 74, 0.29);
    color: #888;
  }

  .head-icon{
    display: block;
    width: 50px;
    height: 50px;
    background-image: url('../assets/user.png');
    background-repeat: no-repeat;
    background-size: 80%;
    background-position:center;
    margin-right: 10px;
  }
  .gender {
    width: 50px;
    height: 50px;
    float: right;
    background-repeat: no-repeat;
    background-size: 50%;
    background-position:center;
  }

  .title{
    line-height: 30px;
    text-align:left;
  }

  .province{
    line-height: 20px;
    text-align: left;
    font-size: 0.8em;
    color: #888;
  }

  .girl {
    background-image: url("../assets/girl.png");
  }

  .boy {
    background-image: url("../assets/boy.png");
  }

  .alien {
    background-image: url("../assets/alien.png");
  }

  .preview{
    position: fixed;
    right: 20px;
    top: 100px;
    border: 1px solid #ccc;
  }

  .preview>img{
    width:400px;
  }
</style>

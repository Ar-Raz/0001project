<template>
    <div id="profile" class='userPanelComp'>
        <div id="profileWrapper" class="maxIs">
            <div class="title">
                <p> پروفایل
                    <i class='fa fa-building-o'></i>

                </p>
            </div>


            <div class="profileForm">


                <form action="" enctype="multipart/form-data">
                  <producer></producer>
                </form>
            
            </div>
        </div>




    </div>

</template>


<script>
    import producer from "./producer/producer.vue";
    export default{
        components:{
          producer
        }
    }

</script>



<style scoped>
.title{
  width: 100%;
  margin-right: 10px;
}
.title p{
  font-size: 20px;
  font-weight: 800;
}
#profile{
  width:90%
}
.profileForm{
  width: 90%;
}
    .updateProfile{
        display: flex;
        width: 100%;
        justify-content: center;
    }
    .profile{
        margin-top:20px
    }
    .profileInput{
        width:60%;
    }
    .profileRow{
        display:flex;
        margin-top:40px;
        align-items: flex-start;
    }
    .profileLabel{
        width:40%;
        display:flex;
        justify-content: flex-end;
    }
    .profileLabel label{
        margin-right:20px
    }
    #profileWrapper{
      padding-top:20px;
      padding-bottom: 20px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .profileInput input{
        border:1px solid rgb(210,214,222);
        padding:5px;
        width:300px;
        color:black
    }
    select{
        width:300px;
        padding:5px;
        border:1px solid rgb(210,214,222);
        background-color: white;
        direction:rtl;
        font-size:15pt;
        font-weight: lighter;
    }
    textarea{
        border:1px solid rgb(210,214,222);
    }
    option{
        font-size:15pt;
        font-weight: lighter;
    }

    @media (max-width:768px)
    {
        .profileRow{
            flex-direction:column;

        }
        .profileRow .profileLabel{
            margin-top:10px;
            margin-bottom:10px
        }
        .profileLabel,.profileInput,.componyBriefIntroductionInput,.componyWordFileds{
            width:100%
        }
        .profileInput input,.profileInput select,.profileInput textarea,.profileInput select{
            width:100%
        }

    }

</style>
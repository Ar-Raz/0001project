<template>
  <div id="mega">
    <div id="megaWrapper">
      <!-- <ul class="singleMega ">
							<li class="headMega" v-for="(cat,ind) in getCats" :key="ind" v-if='ind<6'><a :href="getHref(cat)">{{cat.title}}</a></li>
      </ul>-->
      <div class="headWrapper">
        <div class="headMenuWrapper">
          <div class="singleMenu">
            <div class="title">عنوان دسته بندی</div>
              <ul>
                <li><a href='#'>دسته 1</a></li>
                <li><a href="#">خط تولید پنیر</a></li>
                <li><a href="#">دسته 1</a></li>
                <li><a href="#">دسته</a> </li>
                <li><a href="#">دسته</a></li>
              </ul>
          </div>
          <div class="singleMenu">
            <div class="title">عنوان دسته بندی</div>
              <ul>
                <li><a href='#'>دسته 1</a></li>
                <li><a href="#">خط تولید پنیر</a></li>
                <li><a href="#">دسته 1</a></li>
                <li><a href="#">دسته</a> </li>
                <li><a href="#">دسته</a></li>
              </ul>
          </div>
          <div class="singleMenu">
            <div class="title">عنوان دسته بندی</div>
              <ul>
                <li><a href='#'>دسته 1</a></li>
                <li><a href="#">خط تولید پنیر</a></li>
                <li><a href="#">دسته 1</a></li>
                <li><a href="#">دسته</a> </li>
                <li><a href="#">دسته</a></li>
              </ul>
          </div>
        </div>
        <div class="headMenuWrapper">
          <div class="singleMenu">
            <div class="title">عنوان دسته بندی</div>
              <ul>
                <li><a href='#'>دسته 1</a></li>
                <li><a href="#">خط تولید پنیر</a></li>
                <li><a href="#">دسته 1</a></li>
                <li><a href="#">دسته</a> </li>
                <li><a href="#">دسته</a></li>
              </ul>
          </div>
          <div class="singleMenu">
            <div class="title">عنوان دسته بندی</div>
              <ul>
                <li><a href='#'>دسته 1</a></li>
                <li><a href="#">خط تولید پنیر</a></li>
                <li><a href="#">دسته 1</a></li>
                <li><a href="#">دسته</a> </li>
                <li><a href="#">دسته</a></li>
              </ul>
          </div>
          <div class="singleMenu">
            <div class="title">عنوان دسته بندی</div>
              <ul>
                <li><a href='#'>دسته 1</a></li>
                <li><a href="#">خط تولید پنیر</a></li>
                <li><a href="#">دسته 1</a></li>
                <li><a href="#">دسته</a> </li>
                <li><a href="#">دسته</a></li>
              </ul>
          </div>
        </div>

      </div>
	  
    </div>
  </div>
</template>

<style scoped>
.headWrapper{
  width:100%;
	display:flex;
}
#megaWrapper{
  width:100%;
	display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
#mega {
  margin-top: 50px;
}
ul {
  list-style: none;
    line-height: 1.4rem;
}
li a {
  font-size: 18px;
  text-align:right;
}
li {
    text-align: right;
    line-height:2rem;
}
.headMenuWrapper{
  display:flex;
  justify-content:space-around;
  width:100%;

}
.title{
  text-align:right;
  font-weight:bold;
  font-size:20px;
}
@media (min-width:500px) and (max-width:1000px){
  .headWrapper{
    flex-direction:column
  }
}
@media (max-width:500px){
  .headWrapper{
    flex-direction:column
  }
  .headMenuWrapper{
    flex-direction:column;
    align-items:flex-end
  }
  .singleMenu{
    margin-right:10px;
    margin-top:15px
  }
}
</style>

<script>
export default {
  computed: {
    getCats() {
      return this.$store.getters.getCatsWithSubs;
    },
  },
  methods: {
    getHref(cat) {
      return `/${cat.title}`;
    }
  },
  computed:{
    getCats(){
      return this.$store.getters.getCatsWithSubs
    }
  }
};
</script>
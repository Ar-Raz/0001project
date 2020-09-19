<template>
  <div id="mega">
    <div id="megaWrapper">
      <!-- <ul class="singleMega ">
							<li class="headMega" v-for="(cat,ind) in getCats" :key="ind" v-if='ind<6'><a :href="getHref(cat)">{{cat.title}}</a></li>
      </ul>-->
      <div class="headWrapper">
		  <ul>
			  	<li>دسته 1</li>
        		<li>دسته 2</li>
        		<li>خط تولید </li>
		  </ul>
		  <ul>
			  	<li>دسته 1</li>
        		<li>دسته 2</li>
        		<li>خط تولید </li>

		  </ul>
      </div>
	  <div class="headWrapper">
		  <ul>
			  	<li>دسته 155</li>
        		<li>دسته 2</li>
        		<li>خط تولید </li>
		  </ul>
		  <ul>
			  	<li>دسته 1</li>
        		<li>دسته 25</li>
        		<li>خط تولید پنیر پیتزا</li>
						
		  </ul>
      </div>
	  
    </div>
  </div>
</template>

<style scoped>
.headWrapper{
	display:flex;
	flex-wrap:wrap;
}
#megaWrapper{
	display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
#mega {
  margin-top: 50px;
}
ul {
  list-style: none;
    margin: 10px;
    line-height: 1.4rem;
    display: flex;
    margin: auto;
}
li a {
  font-size: 18px;
  font-weight: bold;
}
li {
  margin: 5px;
    text-align: right;
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
    },
  },
};
</script>
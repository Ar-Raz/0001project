<template>
  <div id="mega">
    <div id="megaWrapper">
      <!-- <ul class="singleMega ">
							<li class="headMega" v-for="(cat,ind) in getCats" :key="ind" v-if='ind<6'><a :href="getHref(cat)">{{cat.title}}</a></li>
      </ul>-->
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
      <ul>
        <li>دسته 1</li>
        <li>دسته 2</li>
        <li>خط تولید </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
#megaWrapper{
	display:flex;
	justify-content: space-between;
}
#mega {
  margin-top: 50px;
}
ul {
  display: flex;
  flex-direction:column;
  padding: 5px;
  flex-wrap: wrap;
  justify-content: space-between;
}
li a {
  font-size: 18px;
  font-weight: bold;
}
li {
  margin: 15px;
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
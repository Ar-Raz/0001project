<template>
  <div id="selectCategory">
    <div id="selectCategoryWrapper">
      <div class="headCategory cats" id="cats">
        <v-select
          placeholder="یک دسته بندی انتخاب کنید"
          dir="rtl"
          @input="changeCategory($event, -1)"
          class="style-chooser"
          label="title"
          :options="cats"
        ></v-select>
        <input type="hidden" name="headCategory" :value="catName" />
      </div>
    </div>
  </div>
</template>
<style scoped>
label {
  text-align: center;
}
.cats {
  display: flex;
  flex-direction: column;
  width: 80%;
  max-width: 500px;
}
.style-chooser .vs__dropdown-toggle {
  direction: rtl !important;
}

input {
  color: black;
  direction: rtl;
  border: 1px solid rgb(210, 214, 222);
  padding: 10px;
}

#selectCategory {
  margin-top: 20px;
  margin-bottom: 20px;
  width: 100%;
}
#selectCategoryWrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}
label {
  margin-bottom: 10px;
}
label:before {
  content: "* ";
  color: red;
  font-size: 20pt;
  font-weight: 900;
}
@media (max-width: 500px) {
  #selectCategoryWrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  #selectCategoryWrapper input,
  #selectCategoryWrapper datalist {
    width: 90%;
  }
}
@media (max-width: 320px) {
  #selectCategoryWrapper label {
    font-size: 15pt;
  }
}
.vs__search {
  cursor: pointer;
}
</style>

<script>
// import vSelect from 'vue-select'
import axios from "axios";
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import { mapActions } from "vuex";

export default {
  props: ["cats"],
  components: {
    vSelect,
  },
  data() {
    return {
      catName: null,
    };
  },
  mounted() {
    console.clear();
    let text;
    const initial = document.querySelector(".vs__selected");
    if (initial == null) {
      return;
    }
    text = initial.innerText;
    const iniIndex = this.cats.findIndex((cat) => {
      return (cat.title = text);
    });
    this.changeCategory(null, this.cats[iniIndex].id);
  },
  methods: {
    async changeCategory(e, id = -1) {
      const loader = document.querySelector("#loader");
      if (id > -1) {
        console.log("here");
        const { data } = await axios.get(`/categories-api/variations/${id}`);
        this.fillCatsFromCreaeProduct(data);
        loader.style.display = "none";
        return;
      }
      console.log("there");

      loader.style.display = "block";
      const { data } = await axios.get(`/categories-api/variations/${e.id}`);
      this.catName = e.title;
      this.fillCatsFromCreaeProduct(data);
      console.log("data data", e);
      loader.style.display = "none";
    },
    ...mapActions(["fillCatsFromCreaeProduct"]),
  },
};
</script>

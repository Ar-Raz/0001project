import createComponent from './components/user/userPanel/createPRoduct/createProduct.vue'
import profile from './components/user/userPanel/profile/profile.vue'
import usersList from './components/user/userPanel/usersList/usersList.vue'
import createBlogPost from "./components/user/userPanel/createBlogPost/createBlogPost.vue"
import category from "./components/user/userPanel/category/category.vue"
export const routes=[
    {path:'/userPanel/createProduct',component:createComponent},
    {path:'/userPanel',component:profile},
    {path:"/userPanel/usersList",component:usersList},
    {path:"/userPanel/createBlogPost",component:createBlogPost},
    {path:"/userPanel/category",component:category}
]
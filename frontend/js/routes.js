import createComponent from './components/user/userPanel/createPRoduct/createProduct.vue'
import profile from './components/user/userPanel/profile/profile.vue'
import usersList from './components/user/userPanel/usersList/usersList.vue'
import createBlogPost from "./components/user/userPanel/createBlogPost/createBlogPost.vue"
import category from "./components/user/userPanel/category/category.vue"
export const routes=[
    {path:'/products/users/createProduct',component:createComponent},
    {path:'/products/users',component:profile},
    {path:"/products/users/usersList",component:usersList},
    {path:"/products/users/createBlogPost",component:createBlogPost},
    {path:"/products/users/category",component:category}
]
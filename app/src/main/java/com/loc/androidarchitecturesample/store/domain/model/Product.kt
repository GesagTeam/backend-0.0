package com.loc.androidarchitecturesample.store.domain.model

 class Product : ArrayList<Product.ProductItem>(){
    data class ProductItem(
        val alpha_two_code: String,
        val country: String,
        val domains: List<String>,
        val name: String,
        val stateprovince: String,
        val web_pages: List<String>
    )
}
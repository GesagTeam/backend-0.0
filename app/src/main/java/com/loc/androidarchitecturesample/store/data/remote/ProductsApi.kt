package com.loc.androidarchitecturesample.store.data.remote

import com.loc.androidarchitecturesample.store.domain.model.Product
import retrofit2.http.GET

interface ProductsApi {

    @GET("Hipo/university-domains-list/master/world_universities_and_domains.json")
    suspend fun getProducts(): List<Product.ProductItem>

}
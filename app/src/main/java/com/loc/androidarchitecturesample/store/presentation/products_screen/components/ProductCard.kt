package com.loc.androidarchitecturesample.store.presentation.products_screen.components

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.loc.androidarchitecturesample.store.domain.model.Product

@Composable
fun ProductCard(modifier: Modifier = Modifier, product: Product.ProductItem) {
    Card(
        modifier = modifier,
        shape = RoundedCornerShape(10.dp),
        elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
        colors = CardDefaults.cardColors(containerColor = Color.White)
    ) {
        Column(modifier = Modifier.padding(15.dp)) {
            Spacer(modifier = Modifier.height(5.dp))
            Text(text = product.name, style = MaterialTheme.typography.titleMedium)
            Text(text = product.country, style = MaterialTheme.typography.titleMedium)
        }
    }
}
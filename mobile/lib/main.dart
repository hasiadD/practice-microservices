import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

// Для Android-емулятора і gateway на комп'ютері: http://10.0.2.2:8080
// Для хмари: https://ваш-gateway-url
const baseUrl = 'http://10.0.2.2:8080';

void main() => runApp(const ShopApp());

class ShopApp extends StatelessWidget {
  const ShopApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
        theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.indigo),
        home: const ProductsPage(),
      );
}

class ProductsPage extends StatefulWidget {
  const ProductsPage({super.key});
  @override
  State<ProductsPage> createState() => _ProductsPageState();
}

class _ProductsPageState extends State<ProductsPage> {
  late Future<List<dynamic>> products;

  @override
  void initState() {
    super.initState();
    products = fetchProducts();
  }

  Future<List<dynamic>> fetchProducts() async {
    final r = await http.get(Uri.parse('$baseUrl/products'));
    return jsonDecode(utf8.decode(r.bodyBytes));
  }

  Future<void> order(int id) async {
    await http.post(Uri.parse('$baseUrl/orders'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'product_id': id}));
    if (!mounted) return;
    ScaffoldMessenger.of(context)
        .showSnackBar(const SnackBar(content: Text('Замовлення створено')));
  }

  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(title: const Text('Каталог')),
        body: FutureBuilder<List<dynamic>>(
          future: products,
          builder: (context, snap) {
            if (snap.hasError) return const Center(child: Text('Помилка мережі'));
            if (!snap.hasData) return const Center(child: CircularProgressIndicator());
            return ListView(children: [
              for (final p in snap.data!)
                ListTile(
                  title: Text(p['name']),
                  subtitle: Text('${p['price']} грн'),
                  trailing: FilledButton(
                    onPressed: () => order(p['id']),
                    child: const Text('Замовити'),
                  ),
                ),
            ]);
          },
        ),
      );
}

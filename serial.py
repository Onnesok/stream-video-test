import 'package:flutter/material.dart';
import 'package:flutter_blue_plus/flutter_blue_plus.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: BluetoothChatScreen(),
    );
  }
}

class BluetoothChatScreen extends StatefulWidget {
  @override
  _BluetoothChatScreenState createState() => _BluetoothChatScreenState();
}

class _BluetoothChatScreenState extends State<BluetoothChatScreen> {
  FlutterBluePlus flutterBlue = FlutterBluePlus.instance;
  BluetoothDevice? connectedDevice;

  @override
  void initState() {
    super.initState();
    scanForDevices();
  }

  void scanForDevices() {
    flutterBlue.scan(timeout: Duration(seconds: 5)).listen((scanResult) {
      print("Found device: ${scanResult.device.name}");
      if (scanResult.device.name == "Raspberry Pi") {
        connectToDevice(scanResult.device);
      }
    });
  }

  void connectToDevice(BluetoothDevice device) async {
    await device.connect();
    setState(() {
      connectedDevice = device;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Bluetooth Chat"),
      ),
      body: Center(
        child: connectedDevice == null
            ? Text("Scanning for devices...")
            : Text("Connected to ${connectedDevice!.name}"),
      ),
    );
  }
}

import 'package:http/http.dart' as http;
import 'dart:io';

void main(List<String> arguments) async {
  var ip = "127.0.0.1:8080";
  if (arguments.isNotEmpty) {
    ip = arguments[0];
  }

  String cmd;
  final client = http.Client();

  while (true) {
    stdout.write('\$ ');
    cmd = stdin.readLineSync() ?? "";
    if (cmd == "exit") {
      break;
    }

    try {
      await client.read(Uri.http(ip, cmd));
    } finally {
       client.close();
      print('=> "$cmd" sent');
    }
  }
}

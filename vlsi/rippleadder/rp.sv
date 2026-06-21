module halfadder(input a, input b, output sum ,output cout);
  assign sum=a^b;
  assign cout=a&b;
endmodule //halfadder
module fulladder(input a, input b, input cin, output sum, output cout);
  wire w1, w2,w3;
  halfadder init1(.a(a),.b(b),.sum(w1),.cout(w2));
  halfadder init2(.a(w1),.b(cin),.sum(sum),.cout(w3));
  assign cout=w2|w3;
endmodule //fulladder 
module rpadder(input [3:0] a,b, input cin , output [3:0]sum ,output cout);
  wire c1,c2,c3; 
  fulladder init3(.a(a[3]),.b(b[3]),.cin(cin),.sum(sum[3]),.cout(c1));
  fulladder init4(.a(a[2]),.b(b[2]),.cin(c1),.sum(sum[2]),.cout(c2));
  fulladder init5(.a(a[1]),.b(b[1]),.cin(c2),.sum(sum[1]),.cout(c3));
  fulladder init6(.a(a[0]),.b(b[0]),.cin(c3),.sum(sum[0]),.cout(cout));
endmodule //rpadder  

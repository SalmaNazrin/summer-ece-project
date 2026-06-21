module testbench;
    reg [3:0] a, b;
    reg cin;
    wire [3:0] sum;
    wire cout;
    
    rpadder uut(.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));
    
    initial begin
      $display("a    b    cin | sum   cout");
        
        a=4'b0101; b=4'b0011; cin=0; #10;
        $display("%b %b  %b  | %b  %b", a, b, cin, sum, cout);
        
        a=4'b1111; b=4'b0001; cin=1; #10;
        $display("%b %b  %b  | %b  %b", a, b, cin, sum, cout);
        
        a=4'b0111; b=4'b0111; cin=0; #10;
        $display("%b %b  %b  | %b  %b", a, b, cin, sum, cout);
        
        a=4'b1000; b=4'b1000; cin=0; #10;
        $display("%b %b  %b  | %b  %b", a, b, cin, sum, cout);
    end
endmodule

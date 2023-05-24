module example
  #(
    parameter WIDTH = 32,
    parameter DEPTH = 16
    )
   (
    input        clk,
    input        en,
    input        d,
    output logic q,
    input        x,
    output       y
    );
   
   logic   y_int;
   
   always_ff @(posedge clk)
   begin
      y_int <= x;
   end
   
   assign y = y_int;

   always_comb
   begin
      
   end

   /*
   always_ff @(posedge clk)
   begin
      if (en)
      begin
         q <= d;
      end
   end
    */

   always_ff @(posedge clk)
     if (en) q <= d;
     else
     begin
        q <= 1'b0;
     end

endmodule
  
  


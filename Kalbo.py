<!--nama file calculaor.php-->
<!DOCTYPE html>
<html>
<head>
 <title>Kalkulator</title>
 <Style type="text/css">
  .tombol{
	  background-color: deepskyblue;
  }
  .tabel{
	  background-color: red;
	  margin: 10px;
	  padding: 10px;
  }
  </Style>
 </head>
 <body>
  <form name="kalkulator">
   
  <table style="background-color: " class="tabel">
   <caption>kalkulator</caption>
   <tr>
    <td>angka 2</td><td>:</td><td><input type="number" name="angka1"></td>
   </tr>
   <tr>
      <td>angka 2</td><td>:</td><td><input type="number" name="angka2"></td>
   </tr>
   <tr>
      <td>angka 2</td><td>:</td><td><input type="number" name="hasil"></td>
   </tr>
   <tr>
    <td colspam="3" align="center">
	 <input class="tombol" type="button" onclick="tambah()" value="  +  ">
     <input class="tombol" type="button" onclick="tambah()" value="  -  ">
	 <input class="tombol" type="button" onclick="tambah()" value="  *  ">
	 <input class="tombol" type="button" onclick="tambah()" value="  /  ">
    </td>
   </tr>
  </table>
 </form>

</body>
</html>
<script type="text/Javascript">
Function tambah() {
 var angka1=parseFloat(Document.kalkulator.angka1.value>;
 var angka2=parseFloat(Document.kalkulator.angka2.value>;
 var hasil= angka1+angka2;
 Document.kalkulator.hasil.value=hasil;
} 
Function kurang() {
 var angka1=parseFloat(Document.kalkulator.angka1.value>;
 var angka2=parseFloat(Document.kalkulator.angka2.value>;
 var hasil= angka1-angka2;
 Document.kalkulator.hasil.value=hasil;
} 
Function kali() {
 var angka1=parseFloat(Document.kalkulator.angka1.value>;
 var angka2=parseFloat(Document.kalkulator.angka2.value>;
 var hasil= angka1*angka2;
 Document.kalkulator.hasil.value=hasil;
} 
Function bagi() {
 var angka1=parseFloat(Document.kalkulator.angka1.value>;
 var angka2=parseFloat(Document.kalkulator.angka2.value>;
 var hasil= angka1/angka2;
 Document.kalkulator.hasil.value=hasil;
} 
</script>

function calcBMI(array) {
    var height1 = parseFloat(array.feet)
    var weight1 = parseFloat(array.weight)
    var sqheight = (height1/100) * (height1/100);
    var value1 = weight1 / sqheight;            
    return value1.toFixed(1)
 }

 function calcBMR(array) {
    var height = parseFloat(array.feet)
    var weight = parseFloat(array.weight)
    if (array.gender === 'male' && array.formula === 'opt1') {
       return Math.round((
          (13.397 * weight) + (4.799 * height) - (5.677 * array.age) + 88.362));
       // TDEE
    } else if (array.gender === 'female' && array.formula === 'opt1') {
       return Math.round((
          (9.247 * weight) + (3.098 * height) - (4.330 * array.age) + 447.593));
       // RDEE
    }
    else {
       return Math.round((
          370 + (21.6*(weight * (1-(array.bodyFat)/100) ))
       ));
    }
 }
 
 function calcResult(array) {
    // alert(array.toString().stringify())
    var activity = parseFloat(array.activity, 10);  
    var height = parseFloat(array.feet)
    var weight = parseFloat(array.weight)
    
    // TDEE   
    if (array.gender === 'male' && array.formula === 'opt1') {
       return Math.round((
          (13.397 * weight) + (4.799 * height) - (5.677 * array.age) + 88.362) * activity);
    // TDEE
    } else if (array.gender === 'female' && array.formula === 'opt1') {
       return  Math.round((
          (9.247 * weight) + (3.098 * height) - (4.330 * array.age) + 447.593) * activity);
    // RDEE
    } else {
       var bodyFat = parseInt(array.bodyFat, 10) / 100;
       var LBM = weight - (weight * bodyFat);
       return Math.round((370 + (21.6 * LBM)) * activity);
    }
 };

 function validInput(array) {
    
    var reg = /^(?:\d*\.\d{1,2}|\d+)$/;
    
    //var reg = /^(0|[1-9]\d*)(\.\d+)?$/;

   //var reg = /^[1-9]\d*(\.\d+)?$/;



    if (array.length > 1) {
    }
    var validation =
       reg.test(array.age) &&
       reg.test(array.weight) &&
       reg.test(array.feet) &&
       reg.test(array.inch);
    return validation;
    };
    
    $(document).ready(function() {            
    $('#opt2Mass').hide();            
    $('input[name=formula]').change(function() {
       var formula = $('input[name=formula]:checked').val();
       if (formula === 'opt1') {
          $('#opt2Mass').hide()
       } else {
          $('#opt2Mass').show()
       };
    });
    
    $('#tdeeCalc input[type=button]').click(function() {
       var inputArray = {
          gender    : $('input[name=gender]:checked').val(),
          formula   : $('input[name=formula]:checked').val(),
          age       : $('#age').val(),
          weight    : $('#weight').val(),
          feet      : $('#feet').val(),
          inch      : $('#inch').val() || '0',
          activity  : $('select option:selected').val(),
          bodyFat   : $('#bodyFat').val()
       };

       // console.log(inputArray[0]);
       // alert(inputArray[0])
    
       $('#alertError p').remove();
       $('#result p').remove();
    
       if (validInput(inputArray)) {
          var result = calcResult(inputArray);
          var BMIresult = calcBMI(inputArray);
          var BMRresult = calcBMR(inputArray);

          $('#result').html(
             '<h3><span>TDEE: </span><p>' + result.toString() + ' </p><b>Calories per day</b></h3>' + '<h3><span>BMI: </span><p>' + BMIresult.toString() + '</p><b> kg/m<sup>2</sup></b></h3>' + '<h3><span>BMR: </span><p>'  + BMRresult.toString() + '</p></h3>' + '<table class="table resultanswer"><thead class="thead-dark"><tr><th scope="col"></th><th scope="col">Mild<span>(0.5kg/week)</span></th><th scope="col">Moderate<span>(0.7kg/week)</span></th><th scope="col">Extreme<span>(1kg/week)</span></th></tr></thead>'
          );
       }
     var reg = /^(?:\d*\.\d{1,2}|\d+)$/;
      // var reg=/^(0|[1-9]\d*)(\.\d+)?$/;
      //var reg = /^[1-9]\d*(\.\d+)?$/;


       if (!reg.test(inputArray.age))
          $('#alertError').append('<p>Invalid age, please try again</p>');
    
       if (!reg.test(inputArray.weight))
          $('#alertError').append('<p>Invalid weight, please try again</p>');
    
       if (!reg.test(inputArray.feet))
          $('#alertError').append('<p>Invalid height, please try again</p>');
    
       if (!reg.test(inputArray.inch))
          $('#alertError').append('<p>Invalid height(in), please try again</p>');
    });
 });
app.controller('MainCtrl', function ($scope, $http) {
    console.log('MainCtrl')
    $scope.inverso_elem = []
    $scope.inverso_clear = function () {
        $scope.inverso_elem = []
        $scope.inverse_res = false
    }

    $scope.inverso = function () {
        console.warn($scope.inverso_elem)
        var pair = $scope.inverso_elem.split(',');
        if(pair.length > 2){
            $scope.inverse_res = "Ingresa sólo dos elementos separados por coma"
        }else{
            pair[0] = parseInt(pair[0])
            pair[1] = parseInt(pair[1])
            console.log(pair)
            $http.post('/inverso', pair)
                .then((res) => {
                    console.info(res.data)
                    $scope.inverse_res = "Inverso: " + res.data.data;
                })
                .catch((e) => {
                    console.error(e)
                })
        }
    }

    $scope.c_elem = []
    $scope.c_mod = []
    $scope.c_clear = function () {
        $scope.c_elem = []
        $scope.c_mod = []
        $scope.chine_res = false
    }

    $scope.chine_post = function () {
        console.log($scope.c_elem)
        console.log($scope.c_mod)
        var elem = $scope.c_elem.map(Number);
        var mod = $scope.c_mod.map(Number);
        console.log(elem)
        console.log(mod)

        $http.post('/chine', [elem, mod])
            .then((res) => {
                console.info(res.data)
                $scope.chine_res_error = false

                $scope.chine_res = res.data.data
            })
            .catch((e) => {
                console.error(e)
                $scope.chine_res_error = true
                $scope.chine_res = false


            })
    }


    $scope.gcd_elem = []

    $scope.gcd_clear = function () {
        $scope.gcd_elem = []
        $scope.gcd_res = false
    }

    $scope.gcd_post = function () {
        var pair = $scope.gcd_elem.split(',');
        pair[0] = parseInt(pair[0])
        pair[1] = parseInt(pair[1])
        $http.post('/gcd_api', pair)
            .then((res) => {
                console.info(res.data)

                $scope.gcd_res = res.data.data
            })
            .catch((e) => {
                console.error(e)



            })
    }

    $scope.clearAll = function () {
        $scope.states = [];
        $scope.inputBoxes = ['', ''];
        $scope.errorBoxes = [];
        $scope.inputCounter = 0;
        $scope.htmlString = '';
        $scope.universe = "1,2,3,hola"
    }



})
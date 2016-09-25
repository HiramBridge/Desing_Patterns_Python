function Pizza () {

	this.salsa = "";
	this.tamanio = "";
	this.relleno = "";

	this.agregar_salsa = function (salsa ) {

		this.salsa = salsa;
	}

	this.agregar_tamanio = function (tamanio ) {

		this.tamanio = tamanio;
	}

	this.agregar_relleno = function (relleno ) {

		this.relleno = relleno;
	}

	this.imprimir = function () {

		print("Sale pizza con tamanio"); 

	}

}

function Construir_Pizza () {

	this.pizza = new Pizza();

	this.construir_salsa = function () {
		this.pizza.agregar_salsa ("roja");
	}
	this.construir_tamanio = function () {
		this.pizza.agregar_tamanio("Grande");
	}
	this.construir_relleno  = function() {
		this.pizza.agregar_relleno("Queso");
	}

	this.get_result = function(){ return this.pizza; }


}


function Cocina () {



	this.construct = function (construct_pizza) {

		construct_pizza.construir_salsa();
		construct_pizza.construir_tamanio();
		construct_pizza.construir_relleno();

		return construct_pizza.get_result(); 
	}

}


function Order () {

	

	var cocina = new Cocina(); 

	var construir_pizza = new  Construir_Pizza();

	var pizza = cocina.construct(construir_pizza);

	pizza.imprimir(); 
}


Order(); 


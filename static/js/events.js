function sayHi() {
    alert('hi');
}

const sayBye = () => {
    alert('bye');
}

const sayByeToPerson = (name) => {
    alert('bye ' + name);
}

// called with: sayBye()
// sayByeToPerson("Bobby")


//vanilla js on click event

// document.querySelector("#add_pee").addEventListener('click', (event) => {
//     alert('clicked the pee button!');

//   });

//jquery on click event
// $('#add_poop').on('click', (event) => {
//     alert('clicked the poop button!');
// });

// const formInputsPee = {
//     "eventType": "pee"
// }

$('.event_button').on('click', (event) => {
    const formInput = {
        "eventType": $(event.target).html()
    };
    $.post("/api/events/add", formInput, (response) => {
        alert(`You have added ${response.eventType} to the schedule`);
    });
});

// const formInputsPoop = {
//     "eventType": "poop"
// }

// $('#add_poop').on('click', () => {
//     alert('clicked the poop button!');
//     $.post("/api/events/add", formInputsPoop, (response) => {
//         console.log(formInputsPoop);
//         alert(response);
//     });
// });

// $.get("/api/events/add", formData, (response) => {
//     alert("The event is ${response.event_type}");

// });
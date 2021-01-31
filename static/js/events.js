$.get("/api/events/add", formData, (response) => {
    alert("The event is ${response.event_type}");

});
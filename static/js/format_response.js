function formatResponse(response) {
    // Dividir la respuesta en puntos y eliminar posibles espacios en blanco al principio o al final de cada punto
    var points = response.split('.').map(point => point.trim()).filter(Boolean);
    // Ordenar los puntos teniendo en cuenta el número al principio de cada punto
    var sortedPoints = points.sort((a, b) => {
        var numA = parseInt(a.split(' ')[0]);
        var numB = parseInt(b.split(' ')[0]);
        return numA - numB;
    });
    // Unir los puntos ordenados en un solo string, separados por saltos de línea
    var formattedResponse = sortedPoints.join('\n');
    return formattedResponse;
}

document.addEventListener("DOMContentLoaded", function(event) {
    var resultText = document.querySelector('.result-text');
    console.log("Respuesta sin formato:", resultText.textContent);
    var formattedResponse = formatResponse(resultText.textContent);
    console.log("Respuesta formateada:", formattedResponse);
    resultText.textContent = formattedResponse;
});
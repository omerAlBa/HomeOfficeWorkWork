module.exports.info = function getProduct(id) {
    return Promise.resolve({
        description: "test-Product",
        fdcId: id,
        foodNutrients: []
    })
}

module.exports.search = function search(term) {
  return axios
    .post("https://api.nal.usda.gov/fdc/v1/search", {
      generalSearchInput: term
    }, {auth})
    .then((response) => response.data['foods'])
}
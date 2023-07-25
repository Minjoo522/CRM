const cities = {
  강남구: [[37.51, 127.04], 0],
  강동구: [[37.52, 127.12], 0],
  강북구: [[37.63, 127.02], 0],
  강서구: [[37.54, 126.85], 0],
  관악구: [[37.47, 126.95], 0],
  광진구: [[37.53, 127.08], 0],
  구로구: [[37.49, 126.88], 0],
  금천구: [[37.44, 126.9], 0],
  노원구: [[37.65, 127.05], 0],
  도봉구: [[37.66, 127.04], 0],
  동대문구: [[37.57, 127.04], 0],
  동작구: [[37.5, 126.94], 0],
  마포구: [[37.56, 126.91], 0],
  서대문구: [[37.57, 126.93], 0],
  서초구: [[37.48, 127.03], 0],
  성동구: [[37.56, 127.039], 0],
  성북구: [[37.58, 127.02], 0],
  송파구: [[37.51, 127.1], 0],
  양천구: [[37.51, 126.86], 0],
  영등포구: [[37.52, 126.89], 0],
  용산구: [[37.53, 126.96], 0],
  은평구: [[37.59, 126.93], 0],
  종로구: [[37.57, 126.98], 0],
  중구: [[37.57, 127.02], 0],
  중랑구: [[37.6, 127.09], 0],
};
// TODO: 딕셔너리로

for (const store_city of store_cities) {
  if (cities.hasOwnProperty(store_city)) {
    cities[store_city][1] += 1;
  }
}

const map = L.map('map').setView([37.55, 126.98], 11.5);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  // attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

for (let key in cities) {
  let circle = L.circle(cities[key][0], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: cities[key][1] * 250,
  }).addTo(map);

  let label = L.marker(circle.getLatLng(), {
    icon: L.divIcon({
      className: 'map_label',
      html: `${key}`,
      iconSize: [50, 20],
      fillOpacity: 0,
    }),
  }).addTo(map);
}

const date = Variable('', {
  poll: [1000, 'date'],
})

const Bar = (monitor = 0) => Widget.Window({
  monitor,
  name: 'bar',
  anchor: ['top', 'right'],
  child: Widget.Label({ label: date.bind() })
})

App.config({
  widnows: [Bar(0), Bar(1)]
})

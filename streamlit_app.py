export default function AgroShieldAI() {
  const crops = [
    {
      name: 'Tomatoes',
      stage: 'Fruiting stage',
      harvest: 'Harvest in ~12 days',
      progress: '70%'
    },
    {
      name: 'Onions',
      stage: 'Bulbing stage',
      harvest: 'Harvest in ~28 days',
      progress: '45%'
    },
    {
      name: 'Rice',
      stage: 'Tillering stage',
      harvest: 'Harvest in ~62 days',
      progress: '20%'
    }
  ];

  return (
    <div className="min-h-screen bg-[#f5f4f1] flex justify-center items-center p-4">
      <div className="w-[390px] bg-[#f5f4f1] rounded-[30px] overflow-hidden shadow-2xl border border-gray-200">

        {/* Header */}
        <div className="bg-gradient-to-b from-[#0b4d2b] to-[#0c3d22] text-white px-5 pt-6 pb-4">
          <div className="flex items-center gap-2">
            <div className="text-2xl">🌿</div>
            <div>
              <h1 className="text-2xl font-bold">AgroShield AI</h1>
              <p className="text-green-100 text-sm">
                Good morning, Suresh · Kandy Region
              </p>
            </div>
          </div>

          {/* Tabs */}
          <div className="flex justify-between mt-6 text-sm font-medium">
            <button className="text-[#5cff8d] border-b-2 border-[#5cff8d] pb-2">
              Dashboard
            </button>
            <button className="text-green-200">Scan</button>
            <button className="text-green-200">AI Chat</button>
            <button className="text-green-200">Market</button>
          </div>
        </div>

        {/* Weather Card */}
        <div className="p-4">
          <div className="bg-gradient-to-br from-[#0f5a34] to-[#164d31] rounded-[24px] p-5 text-white relative overflow-hidden">
            <div className="absolute w-36 h-36 bg-green-300/10 rounded-full -top-10 -right-10"></div>

            <div className="flex justify-between items-start relative z-10">
              <div>
                <h2 className="text-5xl font-bold">28°C</h2>
                <p className="text-green-100 text-lg mt-1">
                  Partly cloudy · Kandy
                </p>
              </div>

              <div className="text-right text-green-100 text-sm">
                Mon, May 24
              </div>
            </div>

            <div className="grid grid-cols-3 gap-3 mt-6 relative z-10">
              <div className="bg-white/10 rounded-xl p-3">
                <p className="text-sm text-green-100">Humidity</p>
                <h3 className="text-2xl font-bold">74%</h3>
              </div>

              <div className="bg-white/10 rounded-xl p-3">
                <p className="text-sm text-green-100">Wind</p>
                <h3 className="text-2xl font-bold">12 km/h</h3>
              </div>

              <div className="bg-white/10 rounded-xl p-3">
                <p className="text-sm text-green-100">Rain</p>
                <h3 className="text-2xl font-bold">30%</h3>
              </div>
            </div>
          </div>

          {/* Alert */}
          <div className="mt-4 border border-yellow-700 bg-[#f5ecd9] rounded-2xl p-4 flex gap-3 items-start">
            <div className="text-2xl">⚠️</div>
            <div>
              <h3 className="font-semibold text-[#6f4c00] text-lg">
                Heavy rain alert — Wednesday
              </h3>
              <p className="text-[#6f4c00] text-sm mt-1">
                Consider early harvesting for ripe tomatoes
              </p>
            </div>
          </div>

          {/* Crops */}
          <div className="mt-6">
            <h2 className="font-bold text-2xl text-[#1d2b1f] mb-4">
              MY CROPS
            </h2>

            <div className="grid grid-cols-2 gap-4">
              {crops.map((crop, index) => (
                <div
                  key={index}
                  className="bg-white rounded-2xl p-4 border border-gray-200 shadow-sm"
                >
                  <div className="flex items-center gap-2 mb-2">
                    <div className="w-3 h-3 rounded-full bg-green-600"></div>
                    <h3 className="font-bold text-lg">{crop.name}</h3>
                  </div>

                  <p className="text-gray-600 text-sm">{crop.stage}</p>

                  <div className="w-full bg-gray-200 rounded-full h-2 mt-3">
                    <div
                      className="bg-green-600 h-2 rounded-full"
                      style={{ width: crop.progress }}
                    ></div>
                  </div>

                  <p className="text-gray-700 text-sm mt-3">
                    {crop.harvest}
                  </p>
                </div>
              ))}

              {/* Add Crop */}
              <div className="border-2 border-dashed border-gray-300 rounded-2xl flex flex-col justify-center items-center text-gray-500 min-h-[170px]">
                <div className="text-4xl">+</div>
                <p className="mt-2 font-medium">Add crop</p>
              </div>
            </div>
          </div>

          {/* Quick Actions */}
          <div className="mt-8">
            <h2 className="font-bold text-2xl text-[#1d2b1f] mb-4">
              QUICK ACTIONS
            </h2>

            <div className="grid grid-cols-2 gap-4">
              <button className="bg-[#0f5a34] text-white rounded-2xl p-5 shadow-lg hover:scale-105 transition-all">
                <div className="text-3xl mb-2">📷</div>
                <h3 className="font-bold text-lg">Scan Disease</h3>
                <p className="text-green-100 text-sm mt-1">
                  Upload crop photo
                </p>
              </button>

              <button className="bg-[#1b7a46] text-white rounded-2xl p-5 shadow-lg hover:scale-105 transition-all">
                <div className="text-3xl mb-2">🤖</div>
                <h3 className="font-bold text-lg">Ask AI</h3>
                <p className="text-green-100 text-sm mt-1">
                  Smart farming assistant
                </p>
              </button>
            </div>
          </div>

          {/* Bottom Navigation */}
          <div className="fixed bottom-6 left-1/2 -translate-x-1/2 bg-white rounded-full shadow-2xl px-8 py-4 flex gap-8 border border-gray-200">
            <button className="text-2xl">🏠</button>
            <button className="text-2xl">📊</button>
            <button className="text-2xl">🌦️</button>
            <button className="text-2xl">👤</button>
          </div>
        </div>
      </div>
    </div>
  );
}

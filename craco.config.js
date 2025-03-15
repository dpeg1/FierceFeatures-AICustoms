// craco.config.js
const path = require('path');

module.exports = {
  webpack: {
    configure: (webpackConfig) => {
      // Include @react-spring modules in Babel transpilation
      webpackConfig.module.rules.push({
        test: /\.(js|jsx)$/,
        include: [
          path.resolve('node_modules/@react-spring/three'),
          path.resolve('node_modules/@react-spring/core'),
          path.resolve('node_modules/@react-spring/animated'),
          path.resolve('node_modules/@react-spring/shared')
        ],
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react'],
            plugins: ['@babel/plugin-proposal-optional-chaining']
          }
        }
      });
      return webpackConfig;
    }
  },
  babel: {
    plugins: [
      "@babel/plugin-proposal-optional-chaining"
    ]
  }
};

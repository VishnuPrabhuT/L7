import vue from '@vitejs/plugin-vue'

/**
 * @type {import('vite').UserConfig}
 */
export default {
  minify: "esbuild",
  mode: "production",
  emitManifest: true,
  emitIndex: true,
  enableRollupPluginVue: true,
  plugins: [vue()]
}

import { defineConfig } from 'vite';
import path from 'path';
import { glob } from 'glob';

const staticFiles = glob.sync("./static/**/*.{css,js}", { dotRelative: true }).map((v) => path.resolve(__dirname, v));

export default defineConfig({
    build: {
        outDir: "../built_static",
        cssCodeSplit: true,
        lib: {
            entry: staticFiles,
            formats: ['es']
        },
        rollupOptions: {
            output: {
                preserveModules: true,
                preserveModulesRoot: path.resolve(__dirname, "./static"),
            }
        },
    },
    root: "./static",
    resolve: {
        alias: [
            { find: "$static", replacement: path.resolve(__dirname, 'static') },
        ]
    },
    // https://vitejs.dev/config/server-options#server-origin
    // examples if you use fontawesome and do not include server option below, the path will resolve as 
    // absolute path of file system which cause 404 error when you load fonts from django page.
    server: {
        origin: 'http://localhost:5173',
    }
})